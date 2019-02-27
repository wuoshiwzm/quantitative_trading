import datetime
import requests
import bs4
# import MySQLdb as mdb
import pymysql


# 股票代码
def obtain_parse_wiki_snp500():
    now = datetime.datetime.utcnow();
    response = requests.get("http://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    # print(response)
    soup = bs4.BeautifulSoup(response.text)

    symbolslist = soup.select('table')[0].select('tr')[1:]
    # print(symbolslist)
    symbols = []
    for i, symbol in enumerate(symbolslist):
        tds = symbol.select('td')

        symbols.append(
            (
                tds[0].select('a')[0].text,  # ticker
                'stock',
                tds[1].select('a')[0].text,  # name
                tds[3].text,  # sector
                'USD', now, now
            )
        )

    # print(symbols)
    # print('test')
    return symbols


# 存入数据库
def insert_snp500_symbols(symbols):
    db_host = 'localhost'
    db_user = 'root'
    db_pass = 'root'
    db_name = 'quantitative_trading'
    # 这里链接mysql 用 mysqlclient
    # con = mdb.connect(
    #     db_host, dbb_user, db_pass, db_name
    # )
    con = pymysql.Connect(
        host=db_host,
        port = 3306,
        user = db_user,
        passwd = db_pass,
        db=db_name,
        charset = 'utf8'
    )


    # print(con)
    # die
    column_str = """ticker,instrument,name,sector,
                                currency,created_date,last_updated_date
                            """
    insert_str = ("%s, " * 7)[:-2]
    final_str = "INSERT INTO symbol (%s) VALUES (%s)" % (column_str, insert_str)
    # print(cur)
    # die

    with con:
        cur = con.cursor()
        cur.executemany(final_str, symbols)
        con.commit()

    print('insert into database:quantitative_trading  table:symbol')


sym = obtain_parse_wiki_snp500()
insert_snp500_symbols(sym)
