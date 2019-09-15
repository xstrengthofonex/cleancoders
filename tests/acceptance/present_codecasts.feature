Feature: Present codecasts
  Scenario: Present no codecasts
    Given no codecasts
    Given user "U"
    And user "U" logged in
    Then the following codecasts will be presented for "U"
    And there will be no codecasts presented

  Scenario: Present viewable codecasts in chronological order
    Given codecasts
    | title | published |
    | A     | 3/1/2014  |
    | B     | 3/2/2014  |
    | C     | 2/18/2014 |
    Given user "U"
    And user "U" logged in
    And with license for "U" able to view "A"
    Then the following codecasts will be presented for "U"
    And codecasts will be presented in chronological order
    | title | picture | description | viewable | downloadable|
    | C | C | C | - | - |
    | A | A | A | + | - |
    | B | B | B | - | - |

  Scenario: Present downloadable codecasts in chronological order
    Given codecasts
    | title | published |
    | A     | 3/1/2014  |
    | B     | 3/2/2014  |
    | C     | 2/18/2014 |
    Given user "U"
    And user "U" logged in
    And with license for "U" able to download "A"
    Then the following codecasts will be presented for "U"
    And codecasts will be presented in chronological order
    | title | picture | description | viewable | downloadable|
    | C | C | C | - | - |
    | A | A | A | - | + |
    | B | B | B | - | - |
