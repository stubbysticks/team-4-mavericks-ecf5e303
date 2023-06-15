*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move N from bottom left corner      0             0             1                     NORTH         0           1           2
Move S from bottom left corner      0             0             1                     SOUTH         0           0           2   
Move E from bottom left corner      0             0             1                     EAST          1           0           2   
Move W from bottom left corner      0             0             1                     WEST          0           0           2   
Move N from top left corner         0             9             1                     NORTH         0           9           2
Move S from top left corner         0             9             1                     SOUTH         0           8           2   
Move E from top left corner         0             9             1                     EAST          1           9           2   
Move W from top left corner         0             9             1                     WEST          0           9           2   
Move N from top right corner        9             9             1                     NORTH         9           9           2
Move S from top right corner        9             9             1                     SOUTH         9           8           2   
Move E from top right corner        9             9             1                     EAST          9           9           2   
Move W from top right corner        9             9             1                     WEST          8           9           2   
Move N from bottom right corner     9             0             1                     NORTH         9           1           2
Move S from bottom right corner     9             0             1                     SOUTH         9           0           2   
Move E from bottom right corner     9             0             1                     EAST          9           0           2   
Move W from bottom right corner     9             0             1                     WEST          8           0           2   
Move N from middle of the board     1             5             1                     NORTH         1           6           2
Move S from middle of the board     1             5             1                     SOUTH         1           4           2
Move E from middle of the board     1             5             1                     EAST          2           5           2
Move W from middle of the board     1             5             1                     WEST          0           5           2
Move N from bottom edge             6             0             1                     NORTH         6           1           2
Move S from bottom edge             6             0             1                     SOUTH         6           0           2   
Move E from bottom edge             6             0             1                     EAST          7           0           2   
Move W from bottom edge             6             0             1                     WEST          5           0           2   
Move N from left edge               0             6             1                     NORTH         0           7           2
Move S from left edge               0             6             1                     SOUTH         0           5           2   
Move E from left edge               0             6             1                     EAST          1           6           2   
Move W from left edge               0             6             1                     WEST          0           6           2   
Move N from top edge                6             9             1                     NORTH         6           9           2
Move S from top edge                6             9             1                     SOUTH         6           8           2   
Move E from top edge                6             9             1                     EAST          7           9           2   
Move W from top edge                6             9             1                     WEST          5           9           2   
Move N from right edge              9             6             1                     NORTH         9           7           2
Move S from right edge              9             6             1                     SOUTH         9           5           2   
Move E from right edge              9             6             1                     EAST          9           6           2   
Move W from right edge              9             6             1                     WEST          8           6           2   


*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}