# GPT2_tho5chu

Vietnamese Poem Generator

Dataset was crawled from website: [Thi Viện](https://www.thivien.net/)

To run, use
```python
from transformers import pipeline

prompt = 'Chiều chiều ra đứng ngõ\n'
generator = pipeline('text-generation', model='winvswon78/gpt2_viet_poem_generation')
results = generator(
    prompt,
    max_new_tokens=50,
    do_sample=True,
    top_k=50,
    top_p=0.95,
    temperature=0.8,
    repetition_penalty=1.2
)
results = results[0]['generated_text']
print()
for line in results.split('\n'):
    print(line)
```
