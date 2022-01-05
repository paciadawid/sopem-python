# Created by dejve at 1/5/2022
Feature: User management

  Scenario: Update user
    Given I have a unique user created
    When I update user using following data
      | key  | value          |
      | name | Tester Testowy |
    Then I see user has a following data
      | key  | value          |
      | name | Tester Testowy |