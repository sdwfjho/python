# python pandas
####  df.merge()
##### no
确定哪个字段作为主键，如果不指定，相同信息的列都会作为拼接依据。
##### leftindex和rightindex
默认为False，就是不以索引作为主键，调整为True就可以了。
##### how
控制拼接方式，默认内连接（inner），left为左连接，right为右连接，outer为外连接，保留所有信息，相同的标签自动为主键。
####  df.concat()

### sqlite3