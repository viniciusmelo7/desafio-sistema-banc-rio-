from datetime import datetime
import pytz

data = datetime.now(pytz.timezone('europe/oslo'))
data2 = datetime.now(pytz.timezone('america/fortaleza'))
print(data)
print(data2)
