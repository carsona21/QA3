import sqlite3

# Function to create the database and a table for the ACCT2110 course
def create_database():
    # Connect to SQLite database (it will create 'quiz.db' if it doesn't exist)
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Create a table named 'ACCT2110' with columns for storing questions and answers
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ACCT2110 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Function to add a question to the ACCT2110 table
def add_question_to_ACCT2110(question, option_a, option_b, option_c, option_d, correct_option):
    # Connect to the existing 'quiz.db' database
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Insert a question with options and the correct answer into the 'ACCT2110' table
    cursor.execute('''
        INSERT INTO ACCT2110 (question, option_a, option_b, option_c, option_d, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_option))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Create the database and the ACCT2110 table
create_database()

# Example of adding a question to the ACCT2110 table
add_question_to_ACCT2110(
   questions = [

    ("What is the purpose of the income statement in accounting?", 
     "To show a company's assets, liabilities, and equity", 
     "To show the inflow and outflow of cash over a period", 
     "To show the financial performance over a period of time", 
     "To list outstanding debts and obligations", 
     "C"),

    ("Which of the following is considered a current asset?", 
     "Equipment", 
     "Accounts Receivable", 
     "Building", 
     "Patents", 
     "B"),

    ("What is the formula for calculating net income?", 
     "Revenue - Expenses", 
     "Assets - Liabilities", 
     "Revenue + Expenses", 
     "Gross Profit - Cost of Goods Sold", 
     "A"),

    ("Which of the following financial statements shows the financial position of a company at a specific point in time?", 
     "Income Statement", 
     "Balance Sheet", 
     "Statement of Cash Flows", 
     "Statement of Retained Earnings", 
     "B"),

    ("In double-entry accounting, every transaction affects:", 
     "Only one account", 
     "At least two accounts", 
     "No accounts", 
     "Unlimited accounts", 
     "B"),

    ("Which of the following is classified as a liability?", 
     "Inventory", 
     "Retained Earnings", 
     "Accounts Payable", 
     "Revenue", 
     "C"),

    ("What type of account is 'Retained Earnings'?", 
     "Asset", 
     "Liability", 
     "Equity", 
     "Revenue", 
     "C"),

    ("Depreciation is used to:", 
     "Determine cash flows", 
     "Allocate the cost of an asset over its useful life", 
     "Record appreciation of assets", 
     "Track changes in inventory", 
     "B"),

    ("Which financial statement reports cash inflows and outflows from operations, investing, and financing?", 
     "Income Statement", 
     "Balance Sheet", 
     "Statement of Cash Flows", 
     "Statement of Retained Earnings", 
     "C"),

    ("If a company has more liabilities than assets, it is said to have:", 
     "Positive equity", 
     "Negative equity", 
     "Neutral equity", 
     "No equity", 
     "B")

]

)

print("Database created with table 'ACCT2110' and example question added.")

import sqlite3

def add_new_table_BMGT3510():
    # Connect to the existing 'quiz.db' database
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # SQL command to create a new table named 'BMGT3510'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS BMGT3510 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def add_question_to_BMGT3510(question, option_a, option_b, option_c, option_d, correct_option):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO BMGT3510 (question, option_a, option_b, option_c, option_d, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_option))
    conn.commit()
    conn.close()

add_question_to_BMGT3510(
questions = [

    ("What is the main purpose of strategic management in business?", 
     "To monitor employee performance", 
     "To plan and execute the company's overall direction and goals", 
     "To manage day-to-day operations", 
     "To handle customer complaints", 
     "B"),

    ("A SWOT analysis helps a business understand its:", 
     "Sales forecasts", 
     "Strengths, Weaknesses, Opportunities, and Threats", 
     "Employee satisfaction", 
     "Customer demographics", 
     "B"),

    ("Which of the following is a key component of a mission statement?", 
     "Vision of the future", 
     "Description of day-to-day tasks", 
     "Company's purpose and core values", 
     "Financial performance targets", 
     "C"),

    ("Porter's Five Forces analysis is used to evaluate:", 
     "Internal financial risks", 
     "External factors in an industry that affect competition", 
     "Employee morale", 
     "Company ownership structure", 
     "B"),

    ("Which type of strategy focuses on offering unique products to a broad market?", 
     "Cost leadership", 
     "Differentiation", 
     "Focus strategy", 
     "Growth strategy", 
     "B"),

    ("A balanced scorecard is a tool used to measure:", 
     "Only financial performance", 
     "Customer satisfaction", 
     "A combination of financial and non-financial metrics", 
     "Employee salaries", 
     "C"),

    ("What is the purpose of conducting a PESTEL analysis?", 
     "To understand political, economic, social, technological, environmental, and legal factors impacting a business", 
     "To determine company budget allocations", 
     "To evaluate customer feedback", 
     "To assess internal strengths and weaknesses", 
     "A"),

    ("Which leadership style involves making decisions without input from others?", 
     "Democratic", 
     "Autocratic", 
     "Laissez-faire", 
     "Transformational", 
     "B"),

    ("In business, 'benchmarking' refers to:", 
     "Setting new company records", 
     "Comparing your company's performance with industry bests or competitors", 
     "Hiring new staff", 
     "Promoting products", 
     "B"),

    ("The BCG Matrix helps managers evaluate business units based on:", 
     "Employee skill sets and performance", 
     "Market growth and market share", 
     "Company assets and liabilities", 
     "Customer demographics", 
     "B")

]
)

# Create the new table 'BMGT3510'

print("Table 'BMGT3510' created successfully.")

def add_new_table_():
    # Connect to the existing 'quiz.db' database
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # SQL command to create a new table named 'BMGT3510'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ECONN4900 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def add_question_to_ECON4900(question, option_a, option_b, option_c, option_d, correct_option):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ECON4900 (question, option_a, option_b, option_c, option_d, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_option))
    conn.commit()
    conn.close()

add_question_to_ECON4900(
questions = [

    ("What is the primary focus of macroeconomics?", 
     "The behavior of individual consumers", 
     "The operations of small businesses", 
     "The economy as a whole", 
     "The management of company finances", 
     "C"),

    ("Which of the following measures the total value of goods and services produced within a country?", 
     "Gross Domestic Product (GDP)", 
     "Consumer Price Index (CPI)", 
     "Net National Product (NNP)", 
     "Balance of Trade", 
     "A"),

    ("What does the term 'inflation' refer to?", 
     "A decrease in the unemployment rate", 
     "An increase in the overall level of prices for goods and services", 
     "A reduction in government spending", 
     "An increase in the value of currency", 
     "B"),

    ("The Phillips Curve illustrates the relationship between:", 
     "Inflation and interest rates", 
     "Unemployment and economic growth", 
     "Inflation and unemployment", 
     "Supply and demand", 
     "C"),

    ("What is fiscal policy primarily concerned with?", 
     "The money supply in the economy", 
     "Taxation and government spending", 
     "The regulation of financial institutions", 
     "Trade relations with other countries", 
     "B"),

    ("A country's balance of payments includes:", 
     "Only exports and imports of goods", 
     "Government spending and taxation", 
     "All economic transactions between residents of the country and the rest of the world", 
     "The domestic employment rate", 
     "C"),

    ("Which of the following is a tool used by central banks to control the money supply?", 
     "Tax incentives", 
     "Interest rate adjustments", 
     "Minimum wage laws", 
     "Government bond issuance", 
     "B"),

    ("When a country experiences hyperinflation, it means that:", 
     "Prices are rising very slowly", 
     "Unemployment is at its lowest level", 
     "Prices are increasing extremely rapidly", 
     "Economic growth is steady", 
     "C"),

    ("The law of supply states that:", 
     "There is an inverse relationship between price and quantity supplied", 
     "There is a direct relationship between price and quantity supplied", 
     "Supply is always independent of price", 
     "Supply only decreases over time", 
     "B"),

    ("What does the term 'opportunity cost' refer to?", 
     "The cost of the most expensive alternative", 
     "The benefit gained from choosing one option over another", 
     "The cost of the next best alternative foregone", 
     "The fixed cost of an investment", 
     "C")

]
)

def add_new_table_():
    # Connect to the existing 'quiz.db' database
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # SQL command to create a new table named 'FIN3210'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS FIN3210 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def add_question_to_FIN3210(question, option_a, option_b, option_c, option_d, correct_option):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO FIN3210 (question, option_a, option_b, option_c, option_d, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_option))
    conn.commit()
    conn.close()

add_question_to_FIN3210(
questions = [

    ("What is the primary goal of corporate finance?", 
     "Maximize shareholder value", 
     "Minimize production costs", 
     "Ensure employee satisfaction", 
     "Comply with government regulations", 
     "A"),

    ("The time value of money principle states that:", 
     "Money received in the future is worth more than money today", 
     "Money received today is worth more than the same amount in the future", 
     "Money has no value over time", 
     "Only cash has a time value", 
     "B"),

    ("Which of the following is an example of a capital budgeting decision?", 
     "Issuing new shares of stock", 
     "Determining which projects to invest in", 
     "Paying off existing debt", 
     "Increasing employee salaries", 
     "B"),

    ("The weighted average cost of capital (WACC) is used to:", 
     "Calculate the total debt of a company", 
     "Measure a company's total revenue", 
     "Determine the company's cost of capital from all sources", 
     "Calculate the value of stock options", 
     "C"),

    ("What is the main purpose of a financial statement analysis?", 
     "To assess a company's historical performance and financial health", 
     "To calculate taxes owed", 
     "To prepare marketing campaigns", 
     "To estimate employee performance", 
     "A"),

    ("A bond's coupon rate is:", 
     "The rate of interest paid by the bond issuer on the bond's face value", 
     "The bond's yield to maturity", 
     "The current market price of the bond", 
     "The principal amount paid at maturity", 
     "A"),

    ("Which of the following best describes 'liquidity'?", 
     "The ease with which an asset can be converted into cash", 
     "A company's profitability ratio", 
     "The amount of debt a company holds", 
     "The total revenue generated over a fiscal year", 
     "A"),

    ("Diversification in investing is important because it:", 
     "Increases potential risk", 
     "Reduces the risk by spreading investments across different assets", 
     "Guarantees profits in any market condition", 
     "Is only applicable to short-term investments", 
     "B"),

    ("The net present value (NPV) of a project is calculated by:", 
     "Summing all cash inflows and outflows", 
     "Discounting future cash flows to the present and subtracting the initial investment", 
     "Adding the total revenue and costs", 
     "Calculating the future value of all inflows", 
     "B"),

    ("What does 'leverage' refer to in finance?", 
     "Using debt to increase potential returns", 
     "Reducing expenses to improve cash flow", 
     "Investing in multiple assets", 
     "The cash flow of a business", 
     "A")
]
)
def add_new_table_():
    # Connect to the existing 'quiz.db' database
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # SQL command to create a new table named 'MKT3400'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MKT3400 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def add_question_to_MKT3400 (question, option_a, option_b, option_c, option_d, correct_option):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO FIN3210 (question, option_a, option_b, option_c, option_d, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_option))
    conn.commit()
    conn.close()

add_question_to_MKT3400(
questions = [

    ("What is the primary goal of marketing?", 
     "To create, communicate, and deliver value to customers", 
     "To reduce production costs", 
     "To manage employee relations", 
     "To comply with regulatory standards", 
     "A"),

    ("The '4 Ps' of marketing are:", 
     "Product, Price, Place, Promotion", 
     "Plan, Produce, Profit, Process", 
     "Product, People, Price, Promotion", 
     "Plan, Perform, Promote, Profit", 
     "A"),

    ("Market segmentation is best described as:", 
     "Grouping customers based on similar characteristics", 
     "Setting prices based on competitor actions", 
     "Promoting products using only digital media", 
     "Expanding a business internationally", 
     "A"),

    ("Which of the following is an example of demographic segmentation?", 
     "Targeting based on geographic region", 
     "Targeting customers by age and gender", 
     "Grouping customers by lifestyle choices", 
     "Targeting customers by purchase behavior", 
     "B"),

    ("The marketing mix is used to:", 
     "Identify the best product suppliers", 
     "Measure the company's financial health", 
     "Create a balance of product, price, place, and promotion", 
     "Evaluate employee performance", 
     "C"),

    ("Which term describes the perceived value or benefit that a customer receives from a product?", 
     "Customer satisfaction", 
     "Brand equity", 
     "Value proposition", 
     "Target market", 
     "C"),

    ("A brand's 'positioning' refers to:", 
     "Its market share", 
     "The place it occupies in the customer's mind relative to competitors", 
     "Its price relative to competitors", 
     "The number of products it offers", 
     "B"),

    ("Which of the following is an example of a push marketing strategy?", 
     "Creating social media content to attract customers", 
     "Advertising directly to end-users", 
     "Offering incentives to retailers to carry and promote products", 
     "Engaging in content marketing", 
     "C"),

    ("The product life cycle stages are:", 
     "Introduction, Growth, Maturity, Decline", 
     "Planning, Production, Promotion, Profit", 
     "Concept, Creation, Distribution, Promotion", 
     "Initiation, Growth, Evaluation, Maturity", 
     "A"),

    ("The term 'customer relationship management (CRM)' refers to:", 
     "Improving the efficiency of marketing campaigns", 
     "Building and maintaining profitable customer relationships", 
     "Setting competitive pricing strategies", 
     "Creating product discounts and promotions", 
     "B")

]
)