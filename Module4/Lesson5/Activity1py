item_name=["pencil","eraser","sharpner","pen"]
stock_count=[32,47,0,54]
stock_dict={item:stock for item,stock in zip(item_name,stock_count)}
print(stock_dict)
new_list=[item for item in item_name if stock_dict[item]!=0]
print(new_list)
buy=input("Which item do you want to buy?: ").strip().lower()
if buy not in item_name or stock_dict[buy]==0:
    exit()
