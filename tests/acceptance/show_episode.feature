Feature: Show episode
  Scenario: Show episode one
    Given codecast
      | title | published | permalink |
      |  A    | 3/1/2014  | episode-1 |
    Given user "U"
    And user "U" logged in
    When the user requests details for codecast episode-1
    Then the presented title is "A" published "3/01/2014
    And with option to purchase viewing license
    And with option to purchase download license
