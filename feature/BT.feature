Feature:BT

  @BT
  Scenario: BT Web Application
    Given I open browser with 'https://www.bt.com/'
    Then I check for the cookies pop up "//a[text()='Accept all cookies']"
    And I hover mouse on "//a[@href='https://www.bt.com/mobile']" and select the option "//a[@href='https://www.bt.com/products/mobile/phones/']"
    Then check the number of banners "3" "//div[@class='flexpay_flexpaycard_container__GnRx9']/div"
    And scroll down until the option visible "//a[text()='View SIM only deals']" and "SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile"
    Then I check element "//*[@id="__next"]//*[text()='30% off']"
    Then I check element "//*[@id="__next"]//*[text()='double data']"
    And I close opened browser