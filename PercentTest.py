# Asking user for language selection
language = input("EN - to continue in English.\nES - para continuar en Español.\nPL - żeby kontynuować po Polsku.")
language = language.lower()

# Defining function to calculate studant grade in percentage
def grade_calculator(language):

    # English version
    if language == "en":
        # Asking for test_name
        test_name = input("What would you like to call this test?    ")
        test_name = test_name.upper()

        # Asking for maxs points on test
        hundred_percent = input("What is the maximum amount of points on this test/assignment/quiz?    ")
        hundred_percent = int(hundred_percent)

        check_another = ""
        check_another = check_another.lower()

        # Making list to gather Student test result
        all_scores = []
        all_scores.append(test_name)

        # Making while loop to allow for the input of aditional Students test results
        while check_another != "done":
            student_name = input("What's the student's name?    ")
            student_name = student_name.capitalize()

            # Asking for students point score
            points = input(f"How many points did {student_name} get?   ")
            points = int(points)

            # Converting points to percentages (float round to two decimal spaces)
            student_score = (points / hundred_percent) * 100
            student_score = float(student_score)
            student_score = f"{student_score:.2f}%"
            
            #Making a sub-list with studant name, point score, and percent score and appending it to the all_scores list
            student = ["Student name: ", student_name, "Score in points: ", points, "Score in %: ", student_score]
            all_scores.append(student)
            
            # Checking if more Student scores need to be added
            check_another = input("type 'done' or press 'enter' to continue:    ")
            check_another = check_another.lower()

        # Printing each sublist from the all_scores list in seperate rows with the test_name at the top
        for score in all_scores:
            print(score)
            
    # Spanish version    
    elif language == "es":
        # Asking for test_name
        test_name = input("¿Como quieres llamar este examen?")
        test_name = test_name.upper()

        # Asking for maxs points on test
        hundred_percent = input("¿Cuántos puntos en total se puede conseguir en este examen?    ")
        hundred_percent = int(hundred_percent)

        check_another = ""
        check_another = check_another.lower()

        # Making list to gather Student test result
        all_scores = []
        all_scores.append(test_name)

        # Making while loop to allow for the input of aditional Students test results
        while check_another != "termine":
            
            # Asking for Students name
            student_name = input("¿Cual es el nombre del estudiante?    ")
            student_name = student_name.capitalize()

            # Asking for students points score
            points = input(f"Cuántos puntos consiguio obtener {student_name}?   ")
            points = int(points)

            # Converting points to percentages (float round to two decimal spaces)
            student_score = (points / hundred_percent) * 100
            student_score = float(student_score)
            student_score = f"{student_score:.2f}%"
            
            #Making a sub-list with studant name, point score, and percent score and appending it to the all_scores list
            student = ["Nombre del estudiante: ", student_name, "Puntos: ", points, "Porcentaje: ", student_score]
            all_scores.append(student)
            
            # Checking if more Student scores need to be added
            check_another = input("escribe la palabra 'termine' para terminar o pulsa 'enter' para continuar:    ")
            check_another = check_another.lower()

        # Printing each sublist from the all_scores list in seperate rows with the test_name at the top
        for score in all_scores:
            print(score)
    
    # Polish version
    elif language == "pl":
        # Asking for test_name
        test_name = input("Jak chcesz nazwać ten test?    ")
        test_name = test_name.upper()
        
        # Asking for maxs points on test
        hundred_percent = input("Jaka jest maksymalna ilosc punktów na tym teście?    ")
        hundred_percent = int(hundred_percent)

        check_another = ""
        check_another = check_another.lower()

        # Making list to gather Student test result
        all_scores = []
        all_scores.append(test_name)
        
        # Making while loop to allow for the input of aditional Students test results
        while check_another != "koniec":
            
            # Asking for Students name
            student_name = input("Jak nazywa się uczeń?    ")
            student_name = student_name.capitalize()

            # Asking for students point score
            points = input(f"Ilę punktów otrzymał {student_name}?   ")
            points = int(points)

            # Converting points to percentages (float round to two decimal spaces)
            student_score = (points / hundred_percent) * 100
            student_score = float(student_score)
            student_score = f"{student_score:.2f}%"
            
            #Making a sub-list with studant name, point score, and percent score and appending it to the all_scores list
            student = ["Imię ucznia: ", student_name, "Otrzymane punkt: ", points, "Punkty w %: ", student_score]
            all_scores.append(student)
            
            # Checking if more Student scores need to be added
            check_another = input("wpisz 'koniec' albo kliknij 'ENTER' aby kontynuować:    ")
            check_another = check_another.lower()

        # Printing each sublist from the all_scores list in seperate rows with the test_name at the top
        for score in all_scores:
            print(score)
            
    # If the input doesn't match any of the languages (en, es, pl) then ask about the language again
    else:
        language = input("EN - to continue in English.\nES - para continuar en Español.\nPL - żeby kontynuować po Polsku.")
        language = language.lower()
        grade_calculator(language)
        
# Calling the grade_calculator function        
grade_calculator(language)

# Letting the user know to press ENTER to exit in EN, ES, PL respectively
if language == "en":
    input("Press ENTER to exit.")
elif language == "es":
    input("Para salir pulsa ENTER")
else:
    input("Wciśnij ENTER żeby wyjść")