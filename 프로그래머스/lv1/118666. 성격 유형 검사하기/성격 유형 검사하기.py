def solution(survey, choices):
    answer = ''
    dictionary = {
        'A': 0, 'N': 0,             
        'C': 0, 'F': 0,          
        'M': 0, 'J': 0,      
        'R': 0, 'T': 0
    }
    
    for i in range(len(survey)):
        if choices[i] < 4:
            dictionary[survey[i][0]] += 4 - choices[i]
        else:
            dictionary[survey[i][1]] += choices[i] - 4
    
    rt = 'R' if dictionary['R'] >= dictionary['T'] else 'T'
    cf = 'C' if dictionary['C'] >= dictionary['F'] else 'F'
    jm = 'J' if dictionary['J'] >= dictionary['M'] else 'M'
    an = 'A' if dictionary['A'] >= dictionary['N'] else 'N'
    answer = rt + cf + jm + an
    
    return answer