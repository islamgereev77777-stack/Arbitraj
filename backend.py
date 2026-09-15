from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import asyncio
app=FastAPI(title='ArbRadar')
EX=['binance','bybit','okx','kraken','coinbase','kucoin','gateio','bitget','mexc','cryptocom']
SY=['BTC/USDT','ETH/USDT','SOL/USDT','XRP/USDT','BNB/USDT']
async def get():
 try: import ccxt.async_support as ccxt
 except: return []
 out=[]
 async def one(n):
  try:
   e=getattr(ccxt,n)({'enableRateLimit':True,'timeout':4000}); t=await e.fetch_tickers(SY)
   for s,x in t.items():
    if x.get('ask') and x.get('bid'): out.append({'exchange':n,'symbol':s,'ask':float(x['ask']),'bid':float(x['bid'])})
   await e.close()
  except: pass
 await asyncio.gather(*(one(x) for x in EX)); return out
@app.get('/api/opportunities')
async def opp():
 t=await get(); g={}
 for x in t:g.setdefault(x['symbol'],[]).append(x)
 rows=[]
 for s,a in g.items():
  if len(a)<2: continue
  b=min(a,key=lambda x:x['ask']); q=max(a,key=lambda x:x['bid'])
  if b['exchange']==q['exchange']: continue
  gross=(q['bid']/b['ask']-1)*100; cost=.20
  rows.append({'symbol':s,'buy_exchange':b['exchange'],'ask':b['ask'],'sell_exchange':q['exchange'],'bid':q['bid'],'gross':gross,'cost':cost,'net':gross-cost})
 return {'rows':sorted(rows,key=lambda x:x['net'],reverse=True)}
app.mount('/',StaticFiles(directory='.',html=True),name='static')
