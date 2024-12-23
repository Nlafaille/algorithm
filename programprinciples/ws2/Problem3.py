big_exam_halls = int(input('How many big exam halls '))
small_exam_halls = int(input('How many small exam halls? '))


number_of_class = int((big_exam_halls * 45 + small_exam_halls * 22) / 25)
print(f"Number of classes: {number_of_class}")


