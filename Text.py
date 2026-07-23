1. Why systems using rule-based processing require explicit “override” conditions

Systems using rule-based processing make decisions in a specified order, and, therefore, require explicit “override” conditions for cases that do not match general conditions. In other words, there is a need to prioritize specific situations such that their outcomes are not regulated by common rules. This prioritization is necessary to ensure that overrides are fulfilled as exceptions.

2. What would happen if the override check was placed after the checks for time and item, as indicated by the student

The problem with placing an override check after time and item checks is that the initial conditions would have been met, thus making the override unnecessary. The override, therefore, would never be reached, and the program would return erroneous results for valid cases. For example, if Aliah places the override check after time or item checks, the override check would not have been reached because the time or item requirements had already been satisfied by a valid student request. As a result, the override would never be triggered.

3. Your thoughts on the conflict example, and how you would change the program to add a higher level override condition

To resolve the conflict in the example, Aliah needs to add a prioritization condition. For example, there may be cases where the student has a teacher’s pass, but the school is closed for cleaning. In this scenario, one can argue that teacher’s passes would not be valid on days when the school is closed for cleaning. By adding such a condition to the rule-based system, the program will be able to distinguish between different student needs and prioritize them based on the specified order. I would implement this change by adding an override to the beginning of the rule list. For example, “if area is closed for official reasons → deny” will be added on top of the existing rules. In this way, the new rule will be prioritized over the others and will always be processed first.
