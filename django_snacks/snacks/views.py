from django.views.generic import TemplateView

class HomePageView(TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['snacks'] = [
      {
        "name": "Cheez-It",
        "description": "A brand of cheese cracker snack made by the Kellogg Company. They come in a variety of flavors such as cheddar, pepper jack, and extra toasty. They are made with real cheese and are typically square-shaped. They are often sold in resealable, portable bags and are a popular snack for both children and adults."
      },
      {
        "name": "Goldfish",
        "description": "Goldfish are a snack made from cheese and shaped like small fish. They are a popular snack for children and are available in a variety of flavors such as cheddar, parmesan, and pepperoni. They are often sold in portable, resealable bags for snacking on the go."
      },
      {
        "name": "Gushers",
        "description": "Gusher is a brand of fruit-flavored snacks made by the Betty Crocker division of General Mills. They are soft, chewy candies filled with fruit juice and come in a variety of flavors such as grape, strawberry, and apple. They are often sold in small, portable pouches and are a popular snack for children. They're often marketed as a fruity and fun way to get a burst of flavor."
      },
      {
        "name": "Popcorn",
        "description": "Popcorn is a type of corn that pops when heated. It is a popular snack food that is made by heating the kernels of corn until they explode, creating a light and fluffy snack. Popcorn can be enjoyed plain, or it can be flavored with butter, salt, or other seasonings. It is a popular snack food in the United States and is often consumed at movie theaters and sporting events. Popcorn is also a popular snack around the world and can be enjoyed in many different ways. "
      },
      {
        "name": "Soda",
        "description": "Soda, also known as pop or carbonated beverage, is a type of sweetened, carbonated soft drink. It is typically made with carbonated water, a sweetener (such as sugar or high fructose corn syrup), and a natural or artificial flavoring. Some of the most popular soda brands in the United States include Coca-Cola, Pepsi, and Sprite. They are widely consumed, and can be found in almost every store and vending machine across the country. Soda is high in sugar and calories, and consuming too much of it can lead to weight gain and other health problems."
      }
    ]

    return context

class AboutPageView(TemplateView):
  template_name = 'about.html'
