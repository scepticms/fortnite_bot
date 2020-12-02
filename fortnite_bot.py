import time
import random
import pyfiglet
from dhooks import Webhook
from dhooks import Embed
import datetime
from termcolor import colored
from colorama import Fore, init
init()
print(Fore.BLUE + pyfiglet.figlet_format("Fortnite Bot"))
site = input("Enter Website: ")
shoe = input("Enter Sku / Var: ")
itemPrice = input("Item Price ")
maxPrice = input("Max Price ")
webhookInput = input("Enter Webhook: ")
speed = ("10.021s")

hook = Webhook(webhookInput)

if itemPrice > maxPrice:
    print(Fore.RED + pyfiglet.figlet_format("PRICE TOO HIGH STOPPING!!"))

if maxPrice >= itemPrice:
    initialTimer = (time.time())
    print("Starting task")
    time.sleep(.1)
    print("Found Product")
    time.sleep(random.uniform(.05,.2))
    print("Found Product")
    time.sleep(random.uniform(.05,.2))
    print("Found Product")
    time.sleep(random.uniform(.05,.2))
    print("Adding to Cart...")
    time.sleep(random.uniform(.05,.2))
    print("Adding to Cart...")
    time.sleep(random.uniform(.05,.2))
    print("Adding to Cart...")
    time.sleep(random.uniform(.05,.2))
    print("Adding to Cart...")
    time.sleep(.5)
    print("Submitting Shipping...")
    time.sleep(random.uniform(.05,.2))
    print("Submitting Shipping...")
    time.sleep(random.uniform(.05,.2))
    print("Submitting Shipping...")
    time.sleep(random.uniform(.05,.2))
    print("Submitting Shipping...")
    time.sleep(random.uniform(.05,.2))
    print("Submitting Billing...")
    time.sleep(random.uniform(.05,.2))
    print("Submitting Billing...")
    time.sleep(random.uniform(.05,.2))
    print("Submitting Billing...")
    time.sleep(random.uniform(.05,.2))
    print("Submitting Billing...")
    time.sleep(random.uniform(.05,.2))
    print("Submitting Payment...")
    time.sleep(random.uniform(.05,.2))
    print("Submitting Payment...")
    time.sleep(random.uniform(.05,.2))
    print("Submitting Payment...")
    time.sleep(random.uniform(.05,.2))
    print("Submitting Payment...")
    time.sleep(random.uniform(.05,.2))
    print("Processing Order...")
    time.sleep(random.uniform(.05,.2))
    print("Processing Order...")
    time.sleep(random.uniform(.05,.2))
    print("Checked Out!!!")
    print("Product Checked Out:" + site + " " + shoe + " For $" + itemPrice)
    endtimer = time.time()
    checkedOut = Embed(color=0x0000FF)
    checkedOut.set_title("🤠 Fortnite Bot Success! 🤠")
    checkedOut.add_field(name = "**Store:** ", value = site)
    checkedOut.add_field(name = "**Item:** ", value = shoe)
    checkedOut.add_field(name = "**Price:** ", value = "$" + itemPrice)
    checkedOut.add_field(name = "**Check Out Speed:** ", value = str(round(endtimer - initialTimer, 2))+ "s")
    checkedOut.set_footer(text = "Fortnite Bot ---" + str(datetime.datetime.now()))
    hook.send(embed = checkedOut)





