from bs4 import BeautifulSoup
import requests

class Analysis(object):
    """
    An object encapsulating an analysis made on a webpage
    """
    def __init__(self, number_of_tables):
        self.number_of_tables = number_of_tables
        self.result_summary = []


class TableSummary(object):
    """
    An object return the individual summaries of the analysis on a single table
    """
    def __init__(self, index, number_of_rows, table_head):
        self.index = index
        self.number_of_rows = number_of_rows
        self.table_head = table_head


def get_page_analysis(url=None):
    response = requests.get(url=url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    tables = soup.find_all('table')
    result = Analysis(len(tables))

    count = 1
    for table in tables:
        table_head = table.find('thead')
        table_rows = table.find_all('tr')
        result.result_summary.append(TableSummary(count, len(table_rows), str(table_head))
        # {
        #     'index': count,
        #     'number_of_rows': len(table_rows),
        #     'table_head': str(table_head),
        #     # 'table_head': table_head.prettify(),
        # }
        )
        count += 1

    return result

def main():
    get_page_analysis()


if __name__ == "__main__":
    main()