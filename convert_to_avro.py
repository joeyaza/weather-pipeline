import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter
from utils import construct_record_name
import logging
logging.basicConfig(level = logging.INFO)

def convert_to_avro(weather_data):
    try:
        logging.info('Creating avro file')
        schema = avro.schema.parse(open("avro_schema/weather_record.avsc", "rb").read())
        writer = DataFileWriter(open(f"records/{construct_record_name(weather_data)}.avro", "wb"), DatumWriter(), schema)
        writer.append(weather_data)
        writer.close()
        logging.info(f'avro file created for record: {construct_record_name(weather_data)}')
    except Exception as e:
        logging.warning(f'An error occured saving the avro file, please see: {e}')



