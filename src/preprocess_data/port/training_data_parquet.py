from cryptomarketdata.port.db_client import   get_data_db_client, Database_Type
from cryptomarketdata.utility import resample_timeframe
from datetime import datetime, timedelta
from ..domains.training_data import splitting_training_and_eval_time_range
import pandas as pd
from ..adapter.TrainingDataStorage import TrainingDataStorage

def prepare_training_data_and_eval_from_parquet(
        exchange:str, 
        symbol:str,
        data_type:Database_Type, 
        data_directory:str, 
        start_date:datetime,
        end_date:datetime,
        data_length: timedelta,
        split_ratio:float, 
        output_folder:str,
        candle_size:str,
        min_candle_population:int,
        )->tuple[str,str]:
    """Prepare training data and eval data from parquet file
    
    
    Args:
        
        exchange (str): exchange name
        symbol (str): symbol name
        data_type (Database_Type): data type
        data_directory (str): data directory
        start_date (datetime): start date
        end_date (datetime): end date
        data_length (timedelta): data length
        split_ratio (float): split ratio
        output_folder (str): output folder
        candle_size (str): candle size e.g. 15Min, 1H, D
        min_candle_population (int): min candle population
    """
    

    db_client = get_data_db_client(
        exchange=exchange, database_type=data_type, data_directory=data_directory
    )
    #Call domain training data to split training and eval time range
    training_time_range, eval_time_range = splitting_training_and_eval_time_range(
        start_date=start_date,
        end_date=end_date,
        data_length=data_length,
        split_ratio=split_ratio,
    )
    
    with TrainingDataStorage(output_folder=output_folder, buffer_size=10000, datafile_prefix=f"{symbol})_training_data") as train_data_storage:
        for training_start_date, training_end_date in training_time_range:
            #convert traing_start_date and training_end_date to int in ms
            training_start_date_ms = int(training_start_date.timestamp() * 1000)
            training_end_date_ms = int(training_end_date.timestamp() * 1000)
            # Get training candles
            candles:pd.Dataframe = db_client.get_candles(symbol=symbol, from_time=training_start_date_ms, to_time=training_end_date_ms)
            # Resample training candles
            candles_sampled:pd.DataFrame = resample_timeframe(
                data = candles,
                tf = candle_size,
            )
            # Filter candles
            if len(candles_sampled) < min_candle_population:
                continue
            # Save training candles
            train_data_storage.save_candles(candles_sampled)

    pass
