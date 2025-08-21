def totalbill(bill_amount,tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    total=round(total,2)
    print("Please pay",total)

totalbill(2000,20)
totalbill(1500,20)
totalbill(200,10)
totalbill(500,40)

