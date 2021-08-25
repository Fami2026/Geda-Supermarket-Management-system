#***(1)Returns all customers from customer table
customers = customer.objects.all()

#(2)Returns first customer in table
firstCustomer = customer.objects.first()

#(3)Returns last customer in table
lastCustomer = customer.objects.last()

#(4)Returns single customer by name
customerByName = customer.objects.get(name='Fami Abrahim')

#***(5)Returns single customer by name
customerById = customer.objects.get(id=1)

#***(6)Returns all orders related to customer (firstCustomer variable set above)
firstCustomer.order_set.all()

#(7)***Returns orders customer name: (Query parent model values)
orders = order.objects.first() 
parentName = orders.customer.name

#(8)***Returns products from products table with value of "Out Door" in category attribute
products = Product.objects.filter(category="Out Door")
products = Product1.objects.filter()


#(9)***Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id') 
greatestToLeast = Product.objects.all().order_by('-id') 


#(10) Returns all products with tag of "Sports": (Query Many to Many Fields)
#productsFiltered = Product.objects.filter(tags__name="Sports")

'''
(11)Bonus
Q: If the customer has more than 1 ball, how would you reflect it in the database?
A: Because there are many different products and this value changes constantly you would most 
likly not want to store the value in the database but rather just make this a function we can run
each time we load the customers profile
'''

#Returns the total count for number of time a "Ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product__name="chocolate").count()

#Returns total count for each product orderd
allOrders = {}

for orders in firstCustomer.order_set.all():
	if orders.product.name in allOrders:
		allOrders[orders.product.name] += 1
	else:
		allOrders[orders.product.name] = 1

#Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(Customer)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()

