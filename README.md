# ArbRadar
Веб-приложение для мониторинга spot-арбитража между Binance, Bybit, OKX, Kraken, Coinbase, KuCoin, Gate.io, Bitget, MEXC и Crypto.com.

Запуск: `pip install -r requirements.txt` затем `uvicorn backend:app --host 0.0.0.0 --port 8000`.
Откройте http://localhost:8000.

Это сканер сигналов, а не гарант прибыли. Перед реальной торговлей нужно учитывать реальные maker/taker комиссии, стакан и проскальзывание, комиссии/сети вывода, задержки и наличие ликвидности. Реальные ордера в этой версии НЕ выставляются.
