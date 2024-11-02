items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def find_item_index(items, item):
  """
  Функция для поиска индекса товара в списке.

  Args:
    items: Список товаров.
    item: Товар, который нужно найти.

  Returns:
    Индекс первого вхождения товара в список, если товар найден.
    None, если товар не найден.
  """
  for i, value in enumerate(items):
    if value == item:
      return i
  return None


for find_item in ['банан', 'груша', 'персик']:
  index_item = find_item_index(items_list, find_item) # Вызываем функцию для поиска индекса товара
  if index_item is not None:
    print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
  else:
    print(f"Товар '{find_item}' не найден в списке.")