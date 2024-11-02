def find_common_participants(group1, group2, separator=","):
  """
  Находит общих участников в двух группах.

  Args:
    group1: Строка с фамилиями участников первой группы, разделенных separator.
    group2: Строка с фамилиями участников второй группы, разделенных separator.
    separator: Разделитель фамилий в строках.

  Returns:
    Список общих участников, отсортированный в алфавитном порядке.
  """
  participants1 = group1.split(separator)
  participants2 = group2.split(separator)
  common_participants = sorted(set(participants1) & set(participants2))
  return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(f"Общие участники: {common_participants}")

# Проверка с другим разделителем:
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {common_participants}")
