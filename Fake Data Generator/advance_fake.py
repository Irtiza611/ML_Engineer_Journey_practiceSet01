from faker import Faker
from faker.providers import BaseProvider, DynamicProvider
import random

fake = Faker()

for _ in range(5):
    print(fake.bothify(text = "???-######-?", letters = "ABCDXYZ"))


class NeuralProvider(BaseProvider):
    def video_category(self):
        return random.choice(["Machine learning", "Vim" , "Linux", "Finance"])

fake.add_provider(NeuralProvider)

print(fake.video_category())

programming_language_provider = DynamicProvider(
    provider_name = "programming_languages",
    elements = ["Python", "GO", "JS", "React","Ruby", "CPP", "C#"]
)

fake.add_provider(programming_language_provider)
print(fake.programming_languages())

