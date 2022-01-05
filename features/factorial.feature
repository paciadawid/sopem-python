# Created by dejve at 1/5/2022
Feature: # Enter feature name here
  # Enter feature description here

  Scenario Outline: # Enter scenario name here
    # Enter steps here

    When I calculate factorial <input>
    Then I see the result <result>
    Examples:
      | input | result |
      | 0     | 1      |
      | 1     | 2      |