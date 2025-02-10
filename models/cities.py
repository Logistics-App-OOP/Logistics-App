class Cities:
    MELBOURNE = 'Melbourne'
    ALICE_SPRINGS = 'Alice Springs'
    PERTH = 'Perth'
    ADELAIDE = 'Adelaide'
    SYDNEY = 'Sydney'
    BRISBANE = 'Brisbane'
    DARWIN = 'Darwin'
 
    @classmethod
    def city_validator(cls, value):
        if value not in [Cities.MELBOURNE, Cities.ADELAIDE, Cities.ALICE_SPRINGS,
                         Cities.PERTH, Cities.SYDNEY, Cities.BRISBANE, Cities.DARWIN]:
            raise ValueError('Invalid city.')
        return value