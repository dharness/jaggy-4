import sys

salesTotal = 0
oldKey = None
payments = []

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    thisKey, thisSale = data

    if oldKey and oldKey != thisKey:
        payments.append({'payment': oldKey, 'amount': salesTotal})
        # print "{0}\t{1}".format(oldKey, salesTotal)
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey != None:
    payments.append({'payment': oldKey, 'amount': salesTotal})
    payments = sorted(payments, key=lambda k: k['amount'], reverse=True)
    output = ["{0}\t{1}".format(p['payment'], p['amount']) for p in payments]
    print "\n".join(output)
