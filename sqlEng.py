
import pandas as pd 

engine = create_engine('sqlite://test.db', echo=True)

df = pd.read_sql('')

stmt = (
    insert(user_table).
    values(name='username', fullname='Full Username')
)