# Engineering Design

**Team members:**

Plan how your code will meet the product requirements. Keep answers brief. 

## Inputs

*List each input and its Python data type. Note the input assumptions.*
int(input()) for Gb
float(input()) for Base price cost

## Processing and decisions

*What calculations and conversions are needed? How will you organize the decisions, including the nested decision?*
subtraction for finding how many additional Gb over the plan (-)
multiplication for each additional Gb over the base plan (*)
addition for both the base plan and the multiplied cost for each Gb (+)
conversion for the excess Gb from integer into float value.

First we need to calculate the additional Gb (if any) and then multiply that excess Gb with the rate of $2 per extra Gb. Then we need to add that multiplied cost with the base plan cost to get the grand total of the bill.

## Output

*What will the program display for each usage category?*
The program will display (1) how many Gb the customer is over the limit (2) how much the customer is over the limit with qualitative description (moderate/high usage) and (3) the total bill costs of the customer.

## Function design

*Give your data-allowance-checking function's name, parameters, and returned result. How will the program use that result?*
qualitative_usage(Gb, Base_Gb)

the returned result should be the subtracted result of the inputed Gb and the Base Gb.

program will use that result by using a boolean function that determines the printing flow: "You are " (Gb over the limit) "GB over your limit." if you go over the limit. or "You are within your data limit." if you are within the limit.
    
    #if 15 > Gb > 10

    #elif Gb > 15

    #else


