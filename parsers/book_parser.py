from locators.book_locators import BookLocators
import re
import logging
class BookParser:

  RATINGS={
        "One":1,
        "Two":2,
        "Three":3,
      "Four":4,
      "Five":5
  }
  def __init__(self,parent):
      self.parent=parent

  def __repr__(self):  # real signature unknown
    return f'{self.name}, ${self.price} {self.rating} stars'

  @property
  def name(self):
      locator=BookLocators.NAME_LOCATOR
      item_link=self.parent.select_one(locator)
      item_name=item_link.attrs['title']
      return item_name
  @property
  def link(self):
      locator=BookLocators.LINK_LOCATOR
      item_link=self.parent.select_one(locator).attrs['href']
      return item_link

  @property
  def price(self):
      locator = BookLocators.PRICE_LOCATOR
      item_price = self.parent.select_one(locator).string

      pattern = '£([0-9]+\.[0-9]+)'
      matcher = re.search(pattern, item_price)
      price = float(matcher.group(1))
      return price

  @property
  def rating(self):
      locator = BookLocators.RATING_LOCATOR
      star_rating_element = self.parent.select_one(locator)
      classes = star_rating_element.attrs['class']
      rating_classes = filter(lambda x: x != 'star-rating', classes)
      rating_class = next(rating_classes)

      rating = BookParser.RATINGS.get(rating_class)
      return rating