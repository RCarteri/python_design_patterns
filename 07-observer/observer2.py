from abc import ABCMeta, abstractmethod

class NewsAgency:
    def __init__(self):
        self.__observers = []
        self.__last_news = None

    def subscribe(self, observer):
        self.__observers.append(observer)

    def unsubscribe(self, observer=None):
        if not observer:
            return self.__observers.pop()
        else:
            return self.__observers.remove(observer)

    def notify_all(self):
        for observer in self.__observers:
            observer.notify(self)

    def add_news(self, news):
        self.__last_news = news

    def show_news(self):
        return f'Last news: {self.__last_news}'

    def subscribers(self):
        return [type(value).__name__ for value in self.__observers]

class SubscriptionType(metaclass=ABCMeta):
    @abstractmethod
    def notify(self):
        pass

class SubscriptionSMS(SubscriptionType):
    def __init__(self, news_agency):
        self.news_agency = news_agency
        self.news_agency.subscribe(self)
    def notify(self, news_agency):
        print(f'{type(self).__name__} has been notified by {self.news_agency.show_news()}')


class SubscriptionEmail(SubscriptionType):
    def __init__(self, news_agency):
        self.news_agency = news_agency
        self.news_agency.subscribe(self)
    def notify(self, news_agency):
        print(f'{type(self).__name__} has been notified by {self.news_agency.show_news()}')


class SubscriptionOther(SubscriptionType):
    def __init__(self, news_agency):
        self.news_agency = news_agency
        self.news_agency.subscribe(self)
    def notify(self, news_agency):
        print(f'{type(self).__name__} has been notified by {self.news_agency.show_news()}')

if __name__ == '__main__':
    news_agency = NewsAgency()
    SubscriptionSMS(news_agency)
    SubscriptionEmail(news_agency)
    SubscriptionOther(news_agency)

    print(f'Subscribers: {news_agency.subscribers()}')
    news_agency.add_news('Hello world!')
    news_agency.notify_all()

    print(f'Unsubscribed: {type(news_agency.unsubscribe()).__name__}')
    print(f'Subscribers: {news_agency.subscribers()}')

    news_agency.add_news('Hello world again!')
    news_agency.notify_all()
