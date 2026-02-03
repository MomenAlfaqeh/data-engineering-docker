{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "17975623-fde1-4d8f-8d57-69bddb3f801a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Read a sample of the data\n",
    "prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'\n",
    "df = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz', nrows=100)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "2f7c72b9-fd00-46be-983a-fe7d6ee66a2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>VendorID</th>\n",
       "      <th>tpep_pickup_datetime</th>\n",
       "      <th>tpep_dropoff_datetime</th>\n",
       "      <th>passenger_count</th>\n",
       "      <th>trip_distance</th>\n",
       "      <th>RatecodeID</th>\n",
       "      <th>store_and_fwd_flag</th>\n",
       "      <th>PULocationID</th>\n",
       "      <th>DOLocationID</th>\n",
       "      <th>payment_type</th>\n",
       "      <th>fare_amount</th>\n",
       "      <th>extra</th>\n",
       "      <th>mta_tax</th>\n",
       "      <th>tip_amount</th>\n",
       "      <th>tolls_amount</th>\n",
       "      <th>improvement_surcharge</th>\n",
       "      <th>total_amount</th>\n",
       "      <th>congestion_surcharge</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2021-01-01 00:30:10</td>\n",
       "      <td>2021-01-01 00:36:12</td>\n",
       "      <td>1</td>\n",
       "      <td>2.10</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>142</td>\n",
       "      <td>43</td>\n",
       "      <td>2</td>\n",
       "      <td>8.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.3</td>\n",
       "      <td>11.80</td>\n",
       "      <td>2.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>2021-01-01 00:51:20</td>\n",
       "      <td>2021-01-01 00:52:19</td>\n",
       "      <td>1</td>\n",
       "      <td>0.20</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>238</td>\n",
       "      <td>151</td>\n",
       "      <td>2</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.00</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.3</td>\n",
       "      <td>4.30</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>2021-01-01 00:43:30</td>\n",
       "      <td>2021-01-01 01:11:06</td>\n",
       "      <td>1</td>\n",
       "      <td>14.70</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>132</td>\n",
       "      <td>165</td>\n",
       "      <td>1</td>\n",
       "      <td>42.0</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>8.65</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.3</td>\n",
       "      <td>51.95</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>2021-01-01 00:15:48</td>\n",
       "      <td>2021-01-01 00:31:01</td>\n",
       "      <td>0</td>\n",
       "      <td>10.60</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>138</td>\n",
       "      <td>132</td>\n",
       "      <td>1</td>\n",
       "      <td>29.0</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>6.05</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.3</td>\n",
       "      <td>36.35</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>2021-01-01 00:31:49</td>\n",
       "      <td>2021-01-01 00:48:21</td>\n",
       "      <td>1</td>\n",
       "      <td>4.94</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>68</td>\n",
       "      <td>33</td>\n",
       "      <td>1</td>\n",
       "      <td>16.5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>4.06</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.3</td>\n",
       "      <td>24.36</td>\n",
       "      <td>2.5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   VendorID tpep_pickup_datetime tpep_dropoff_datetime  passenger_count  \\\n",
       "0         1  2021-01-01 00:30:10   2021-01-01 00:36:12                1   \n",
       "1         1  2021-01-01 00:51:20   2021-01-01 00:52:19                1   \n",
       "2         1  2021-01-01 00:43:30   2021-01-01 01:11:06                1   \n",
       "3         1  2021-01-01 00:15:48   2021-01-01 00:31:01                0   \n",
       "4         2  2021-01-01 00:31:49   2021-01-01 00:48:21                1   \n",
       "\n",
       "   trip_distance  RatecodeID store_and_fwd_flag  PULocationID  DOLocationID  \\\n",
       "0           2.10           1                  N           142            43   \n",
       "1           0.20           1                  N           238           151   \n",
       "2          14.70           1                  N           132           165   \n",
       "3          10.60           1                  N           138           132   \n",
       "4           4.94           1                  N            68            33   \n",
       "\n",
       "   payment_type  fare_amount  extra  mta_tax  tip_amount  tolls_amount  \\\n",
       "0             2          8.0    3.0      0.5        0.00           0.0   \n",
       "1             2          3.0    0.5      0.5        0.00           0.0   \n",
       "2             1         42.0    0.5      0.5        8.65           0.0   \n",
       "3             1         29.0    0.5      0.5        6.05           0.0   \n",
       "4             1         16.5    0.5      0.5        4.06           0.0   \n",
       "\n",
       "   improvement_surcharge  total_amount  congestion_surcharge  \n",
       "0                    0.3         11.80                   2.5  \n",
       "1                    0.3          4.30                   0.0  \n",
       "2                    0.3         51.95                   0.0  \n",
       "3                    0.3         36.35                   0.0  \n",
       "4                    0.3         24.36                   2.5  "
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "768ce188-049b-4224-8d48-f5e94fdf1e0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4aa4bb3c-f667-4f3e-aa4e-c353bca28b0f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     1\n",
       "1     1\n",
       "2     1\n",
       "3     1\n",
       "4     2\n",
       "     ..\n",
       "95    2\n",
       "96    2\n",
       "97    2\n",
       "98    2\n",
       "99    2\n",
       "Name: VendorID, Length: 100, dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['VendorID']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c3f81718-335d-4bb3-8438-692a5b488234",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[2K\u001b[2mResolved \u001b[1m118 packages\u001b[0m \u001b[2min 2.15s\u001b[0m\u001b[0m                                       \u001b[0m\n",
      "\u001b[2K\u001b[2mPrepared \u001b[1m3 packages\u001b[0m \u001b[2min 1.46s\u001b[0m\u001b[0m                                             \n",
      "\u001b[2K\u001b[2mInstalled \u001b[1m3 packages\u001b[0m \u001b[2min 55ms\u001b[0m\u001b[0m                                \u001b[0m\n",
      " \u001b[32m+\u001b[39m \u001b[1mgreenlet\u001b[0m\u001b[2m==3.3.1\u001b[0m\n",
      " \u001b[32m+\u001b[39m \u001b[1mpsycopg-pool\u001b[0m\u001b[2m==3.3.0\u001b[0m\n",
      " \u001b[32m+\u001b[39m \u001b[1msqlalchemy\u001b[0m\u001b[2m==2.0.46\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "!uv add sqlalchemy \"psycopg[binary,pool]\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "e17ab379-e148-441f-8f11-8f699f644338",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[2K\u001b[2mResolved \u001b[1m119 packages\u001b[0m \u001b[2min 921ms\u001b[0m\u001b[0m                                       \u001b[0m\n",
      "\u001b[2K\u001b[2mPrepared \u001b[1m1 package\u001b[0m \u001b[2min 1.56s\u001b[0m\u001b[0m                                              \n",
      "\u001b[2K\u001b[2mInstalled \u001b[1m1 package\u001b[0m \u001b[2min 12ms\u001b[0m\u001b[0m.11                              \u001b[0m\n",
      " \u001b[32m+\u001b[39m \u001b[1mpsycopg2-binary\u001b[0m\u001b[2m==2.9.11\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "!uv add psycopg2-binary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "b1e35dee-7846-40ee-8a61-8f887c4a2e13",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy import create_engine\n",
    "engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "b705899b-3557-48a1-86b8-89db5c0bcdfd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "CREATE TABLE yellow_taxi_data (\n",
      "\t\"VendorID\" BIGINT, \n",
      "\ttpep_pickup_datetime TEXT, \n",
      "\ttpep_dropoff_datetime TEXT, \n",
      "\tpassenger_count BIGINT, \n",
      "\ttrip_distance FLOAT(53), \n",
      "\t\"RatecodeID\" BIGINT, \n",
      "\tstore_and_fwd_flag TEXT, \n",
      "\t\"PULocationID\" BIGINT, \n",
      "\t\"DOLocationID\" BIGINT, \n",
      "\tpayment_type BIGINT, \n",
      "\tfare_amount FLOAT(53), \n",
      "\textra FLOAT(53), \n",
      "\tmta_tax FLOAT(53), \n",
      "\ttip_amount FLOAT(53), \n",
      "\ttolls_amount FLOAT(53), \n",
      "\timprovement_surcharge FLOAT(53), \n",
      "\ttotal_amount FLOAT(53), \n",
      "\tcongestion_surcharge FLOAT(53)\n",
      ")\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "58a7cd05-dda3-4e4a-9509-ce75a793dcec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "991598b8-3aa1-47dc-9784-ec70bbf9d56e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'dtype' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[31]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[32m      1\u001b[39m df_iter = pd.read_csv(\n\u001b[32m      2\u001b[39m     prefix + \u001b[33m'\u001b[39m\u001b[33myellow_tripdata_2021-01.csv.gz\u001b[39m\u001b[33m'\u001b[39m,\n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m     dtype=\u001b[43mdtype\u001b[49m,\n\u001b[32m      4\u001b[39m     parse_dates=parse_dates,\n\u001b[32m      5\u001b[39m     iterator=\u001b[38;5;28;01mTrue\u001b[39;00m,\n\u001b[32m      6\u001b[39m     chunksize=\u001b[32m100000\u001b[39m\n\u001b[32m      7\u001b[39m )\n",
      "\u001b[31mNameError\u001b[39m: name 'dtype' is not defined"
     ]
    }
   ],
   "source": [
    "df_iter = pd.read_csv(\n",
    "    prefix + 'yellow_tripdata_2021-01.csv.gz',\n",
    "    dtype=dtype,\n",
    "    parse_dates=parse_dates,\n",
    "    iterator=True,\n",
    "    chunksize=100000\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "22fdbda6-d442-4d89-ad57-32724ac7e1d2",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df_iter' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[32]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mfor\u001b[39;00m df_chunk \u001b[38;5;129;01min\u001b[39;00m \u001b[43mdf_iter\u001b[49m:\n\u001b[32m      2\u001b[39m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;28mlen\u001b[39m(df_chunk))\n",
      "\u001b[31mNameError\u001b[39m: name 'df_iter' is not defined"
     ]
    }
   ],
   "source": [
    "for df_chunk in df_iter:\n",
    "    print(len(df_chunk))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "922aafe5-ebcc-4127-8d57-6ddbb6bd22ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[2mResolved \u001b[1m120 packages\u001b[0m \u001b[2min 4ms\u001b[0m\u001b[0m\n",
      "\u001b[2mAudited \u001b[1m13 packages\u001b[0m \u001b[2min 2ms\u001b[0m\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "!uv add tqdm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dece0228-3c42-4964-a49b-48972a4d45b6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
