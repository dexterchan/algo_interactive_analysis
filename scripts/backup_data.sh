#!/bin/sh
backupdate=$(date '+%Y%m%d')
tar czvf  data_process_historical_data_${backupdate}.tgz binance* kraken*