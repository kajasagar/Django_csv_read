from django.shortcuts import render
from django.views import View
import csv
from int_deck.models import Card


# Create your views here.
class CreateDeck(View):

    def get(self, request, *args, **kwargs):
        with open("/Users/sagarkaja/PycharmProjects/Init_deck/Deck/WORDDICTIONARY.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = Card.objects.get_or_create(
                    word=row[0],
                    buzz_word_one=row[1],
                    buzz_word_two=row[2],
                    buzz_word_three=row[3],
                    buzz_word_four=row[4]
                )
            deck= Card.objects.all()

        return render(request, "deck_detail.html", {'deck': deck})
