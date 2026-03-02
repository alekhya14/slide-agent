def validate_deck(deck_spec):
    errors = []

    for slide in deck_spec.slides:
        if len(slide.bullets) > 6:
            errors.append(f"Slide '{slide.title}' has too many bullets.")

        if slide.chart:
            if len(slide.chart.categories) != len(slide.chart.values):
                errors.append(f"Chart mismatch on slide '{slide.title}'")

    return errors