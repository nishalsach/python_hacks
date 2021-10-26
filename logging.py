import logging

# Create and configure logger
logging.basicConfig(
    filename= (home_dir / 'logs' / (today_date+'_validation_notebook.log')),
    format='%(asctime)s %(message)s\n',
    filemode='w')
  
# Creating an object
logger=logging.getLogger()
  
# Setting the threshold of logger to DEBUG - can also set to WARNING, CRITICAL, etc.
logger.setLevel(logging.DEBUG)

# Now just log with this in your code
logger.info(f"Data input complete. Shape of data: {data_shape}.")