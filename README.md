# finki-vi-2020

## Tasks 

### Gradebook Problem 1 (0 / 4)
Дефинирајте речник students во кој ќе се чуваат информации за предметите кои ги полагале студентите.
Од стандарден влез се читаат информации за име, презиме, број на индекс, предмет, поени од теоретски дел,
 поени од практичен дел и поени од лабораториски вежби. Може да се вчитаат информации за неограничен број студенти.
  Вчитувањето информации завршува кога ќе се прочита клучниот збор end.
  Пополнете го речникот students со вчитаните информации.

Потоа, за секој од студентите да се испечати името и презимето, и оцената за секој од предметите кои ги има полагано.

Оцената се пресметува на следниот начин:

[0, 50] - 5

(50, 60] - 6

(60, 70] - 7

(70, 80] - 8

(80, 90] - 9

(90, 100] - 10

#### Sample input:
```Alice,Doe,141414,Artificial Intelligence,40,40,5
Alice,Doe,141414,Machine Learning,30,40,10
Lewis,Smith,141415,Robotics,40,30,10
Lewis,Smith,141415,Bioinformatics,40,30,10
George,Williams,123456,Artificial Intelligence,20,40,9
James,Brown,123457,Artificial Intelligence,25,30,3
William,Williams,123458,Artificial Intelligence,10,45,8
Elle,Brown,123459,Artificial Intelligence,45,10,7
end
```
#### Sample output:
```Student: Alice Doe
    Artificial Intelligence: 9
    Machine Learning: 8

Student: Lewis Smith
    Robotics: 8
    Bioinformatics: 8

Student: George Williams
    Artificial Intelligence: 7

Student: James Brown
    Artificial Intelligence: 6

Student: William Williams
    Artificial Intelligence: 7

Student: Elle Brown
    Artificial Intelligence: 7
```
