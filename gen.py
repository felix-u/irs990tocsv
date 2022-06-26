from bs4 import BeautifulSoup
import csv

# SOURCE FILE
xml_file = "change/this/path/to/file.xml"
# OUTPUT FILE
csv_file = "change/this/path/to/output.csv"

fields = {
    # Name of column        # Where to find this data in XML
    "Organization Name":    ["BusinessName", "BusinessNameLine1Txt"],
    "Project Name":         ["Desc"],
    "Address 1":            ["Filer", "USAddress", "AddressLine1Txt"],
    "City":                 ["Filer", "USAddress", "CityNm"],
    "State":                ["Filer", "USAddress", "StateAbbreviationCd"],
    "Zip":                  ["Filer", "USAddress", "ZIPCd"],

    "Tax year":             ["ReturnHeader", "TaxYr"],
    "Voting members in governing party":
                            ["IRS990", "VotingMembersGoverningBodyCnt"],
    "Number of invididuals employed":
                            ["IRS990", "TotalEmployeeCnt"],
    "Volunteers":           ["IRS990", "TotalVolunteersCnt"],
    "Net unrelated business revenue":
                            ["IRS990", "NetUnrelatedBusTxblIncmAmt"],
    "Contributions and grants":
                            ["IRS990", "CYContributionsGrantsAmt"],
    "Program service revenue":
                            ["IRS990", "CYProgramServiceRevenueAmt"],
    "Investment income":    ["IRS990", "CYInvestmentIncomeAmt"],
    "Total revenue":        ["IRS990", "CYTotalRevenueAmt"],
    "Grants and similar amounts paid":
                            ["IRS990", "CYGrantsAndSimilarPaidAmt"],
    "Salaries, other compensation,":
                            ["IRS990", "CYSalariesCompEmpBnftPaidAmt"],
    "Total fundraising expenses":
                            ["IRS990", "CYTotalProfFndrsngExpnsAmt"],
    "Other expenses":       ["IRS990", "CYOtherExpensesAmt"],
    "Total expenses":       ["IRS990", "CYTotalExpensesAmt"],
    "Revenue less expenses":
                            ["IRS990", "CYRevenuesLessExpensesAmt"],
    "Total assets end of year":
                            ["IRS990", "TotalAssetsEOYAmt"],
    "Total liabilities end of year":
                            ["IRS990", "TotalLiabilitiesEOYAmt"],
    "Net assets or fund balances end":
                            ["IRS990", "NetAssetsOrFundBalancesEOYAmt"],
    "Total assets beginning of year":
                            ["IRS990", "TotalAssetsBOYAmt"],
    "Total liabilities beginning of year":
                            ["IRS990", "TotalLiabilitiesBOYAmt"],
    "Net assets or fund balances":
                            ["IRS990", "NetAssetsOrFundBalancesBOYAmt"],
}


with open(xml_file, "r", encoding="utf8") as xml:
    contents = xml.read()
    soup = BeautifulSoup(contents, "xml")

    # get values from attributes
    values = []
    for i in range(len(fields)):
        field = list(fields.keys())[i]
        attrs = list(fields.values())[i]
        val = getattr(soup, attrs[0])
        for attr in range(len(fields[field]) - 1):
            val = getattr(val, attrs[attr+1])
        val = (val.next).replace('\n', '')
        values.append(val)

    # write csv
    with open(csv_file, mode='w') as csv_file:
        csvWriter = csv.writer(csv_file, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow(list(fields.keys()))
        csvWriter.writerow(values)
