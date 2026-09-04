import pytest
from playwright.sync_api import Page,expect

def test_statictable(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # locating table
    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    # count total number of rows in table
    rows = table.locator("tr")   # equals to "table[name='BookTable'] tbody tr"
    expect(rows).to_have_count(7)

    row_count=rows.count()
    print("Number of rows: ",row_count)

    # count total number of columns/headers in table
    columns = rows.locator("th")  # equals to "table[name='BookTable'] tbody tr th"
    expect(columns).to_have_count(4)

    column_count=columns.count()
    print("Total number of columns: ", column_count)

    # read all the data from second row of the table
    second_row_cell = rows.nth(2).locator('td')
    second_row_texts = second_row_cell.all_inner_texts()
    print("Second row data: ",second_row_texts) # ['Learn Java', 'Mukesh', 'Java', '500']

    expect(second_row_cell).to_have_text(['Learn Java', 'Mukesh', 'Java', '500'])

    print("printing second row data......")
    for text in second_row_texts:
        print(text)

    # read all the data from the table (Excluding header)
    print("Printing data from all rows and columns excluding headers")
    all_row_data = rows.all()
    for row in all_row_data[1:]:
        cols=row.locator("td").all_inner_texts()
        print(cols)

    # print book names where Author name is Mukesh
    print("Printing book names written by Mukesh")
    for row in all_row_data[1:]:
        author_name=row.locator("td").nth(1).inner_text()   # nth(1) refers author name column
        if author_name=="Mukesh":
            book_name=row.locator("td").nth(0).inner_text()
            print(f"{author_name} \t{book_name}")

    # calculate total price of all the books
    # print("Printing data from all rows and columns excluding headers")
    total_price=0
    for row in all_row_data[1:]:
        price = row.locator("td").nth(3).inner_text()
        total_price+=int(price)        # total_price=total_price+int(price)
        print("Total Price: ", total_price)



# pytest day25-test_statictable.py -s -v --headed