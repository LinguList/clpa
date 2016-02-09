# types we distinguish
types = ["marker","tone","vowel","diphtong", "consonant"]

# place we distinguish
places = ['advanced_alveolar',
 'advanced_central_rounded',
 'advanced_central_unrounded',
 'advanced_front_unrounded',
 'advanced_lateral',
 'alveolar',
 'alveolar_to_alveolopalatal',
 'alveolar_to_bilabial',
 'alveolar_to_dental',
 'alveolar_to_interdental',
 'alveolar_to_palatal',
 'alveolar_to_retroflex',
 'alveolar_to_velar',
 'alveolopalatal',
 'back_rounded',
 'back_rounded_to_central_unrounded',
 'back_rounded_to_front',
 'back_rounded_to_front_unrounded',
 'back_rounded_to_labiovelar',
 'back_rounded_to_palatal',
 'back_unrounded',
 'back_unrounded_to_back_rounded',
 'back_unrounded_to_central',
 'back_unrounded_to_palatal',
 'bilabial',
 'bilabial_to_alveolar',
 'bilabial_to_lateral',
 'bilabial_to_postalveolar',
 'bilabial_to_velar',
 'central_rounded',
 'central_unrounded',
 'central_unrounded_to_back_rounded',
 'central_unrounded_to_front',
 'central_unrounded_to_palatal',
 'central_unrounded_to_rounded',
 'dental',
 'dental_to_labiodental',
 'dental_to_palatal',
 'dental_to_postalveolar',
 'dental_to_velar',
 'epiglottal',
 'fall',
 'fall-rise',
 'flat',
 'front_rounded',
 'front_rounded_to_back',
 'front_rounded_to_central_unrounded',
 'front_rounded_to_unrounded',
 'front_unrounded',
 'front_unrounded_to_back_rounded',
 'front_unrounded_to_central',
 'front_unrounded_to_palatal',
 'glottal',
 'interdental',
 'labiodental',
 'labiodental_to_postalveolar',
 'labiopalatal',
 'labiovelar',
 'laminal_alveolar',
 'laminal_alveolar_to_alveolopalatal',
 'laminal_alveolar_to_laminal_postalveolar',
 'laminal_postalveolar',
 'lateral',
 'morpheme_boundary',
 'nasal_vowel',
 'palatal',
 'palatal_to_alveolopalatal',
 'palatal_to_dental',
 'palatal_to_front_unrounded',
 'palatal_to_postalveolar',
 'palatal_to_velar',
 'palatoalveolar',
 'pharyngeal',
 'placeless',
 'postalveolar',
 'postalveolar_to_velar',
 'retracted_alveolar',
 'retroflex',
 'rise',
 'rise-fall',
 'uvular',
 'velar',
 'velar_to_labiodental',
 'word_boundary',
 'zero']

manners = ['affricate',
 'affricate_to_affricate',
 'affricate_to_fricative',
 'affricate_to_stop',
 'approximant',
 'click',
 'ejective',
 'ejective_to_affricate',
 'flap',
 'fricative',
 'fricative_to_affricate',
 'fricative_to_stop',
 'glide_to_higher_mid',
 'high',
 'high_glide_to_higher_mid',
 'high_to_glide',
 'high_to_higher_mid',
 'high_to_low',
 'high_to_lower_mid',
 'high_to_mid',
 'higher_low',
 'higher_low_to_high',
 'higher_mid',
 'higher_mid_glide_to_high',
 'higher_mid_glide_to_higher_mid',
 'higher_mid_glide_to_low',
 'higher_mid_to_glide',
 'higher_mid_to_high',
 'higher_mid_to_lower_high',
 'higher_mid_to_mid',
 'implosive',
 'implosive_affricate',
 'lateral_approximant',
 'lateral_approximant_to_fricative',
 'low',
 'low_to_glide',
 'low_to_high',
 'low_to_high_glide',
 'low_to_higher_mid',
 'low_to_lower_high',
 'lower_high',
 'lower_high_to_high_glide',
 'lower_high_to_lower_mid',
 'lower_mid',
 'lower_mid_to_glide',
 'lower_mid_to_high',
 'lower_mid_to_high_glide',
 'lowered_higher_low',
 'lowered_low',
 'lowered_lower_mid',
 'mid',
 'mid_approximant',
 'mid_glide_to_high',
 'mid_to_high',
 'mid_to_higher_mid',
 'nasal',
 'nasal_spirant',
 'raised_high',
 'raised_higher_mid',
 'raised_low',
 'raised_lower_mid',
 'raised_mid',
 'stop',
 'stop_to_affricate',
 'stop_to_implosive',
 'trill',
 'trill_to_affricate']

miscas = [ 'ATR',
 'RTR',
 'apical',
 'breathy',
 'breathy_long',
 'devoiced',
 'glottalized',
 'glottalized_nasalized',
 'high',
 'interrupted',
 'interrupted_nasalized',
 'low',
 'mid',
 'muffled',
 'nasalized',
 'pharyngealized',
 'pharyngealized_glottalized',
 'pharyngealized_nasalized',
 'plain',
 'postnasalized',
 'retracted',
 'retroflex',
 'retroflex_nasalized',
 'voiced',
 'voiced_long',
 'voiced_to_voiceless',
 'voiceless',
 'voiceless_extra_long',
 'voiceless_long',
 'voiceless_to_voiced',
 'with_frication']

miscbs = [
 'S_accompaniment',
 'Z_accompaniment',
 'affricative',
 'alveolar_prenasalized',
 'alveolar_prenasalized_k_accompaniment',
 'aspirated',
 'aspirated_labialized',
 'aspirated_labialized_prenasalized',
 'aspirated_palatalized',
 'aspirated_prenasalized',
 'aspirated_q_accompaniment',
 'breathy',
 'breathy_long',
 'consonantal',
 'creaky',
 'creaky_long',
 'd_accompaniment',
 'devoiced',
 'extra_long',
 'extra_short',
 'glottalized',
 'glottalized_kx_accompaniment',
 'glottalized_labialized',
 'glottalized_lateral',
 'glottalized_palatalized',
 'glottalized_prenasalized',
 'glottalized_q_accompaniment',
 'preaspirated',
 'heavy',
 'high',
 'kx_accompaniment',
 'l_accompaniment',
 'labial_prenasalized',
 'labial_prenasalized_G_accompaniment',
 'labialized',
 'labialized_labialized',
 'labialized_prenasalized',
 'labialized_tense',
 'labialized_velar_prenasalized',
 'labialized_velarized',
 'labialized_voiced_aspirated',
 'labiopalatalized',
 'lateral',
 'lateral_glottalized',
 'lax',
 'lenis',
 'long',
 'long_breathy',
 'low',
 'mid',
 'nasalized',
 'nasalized_palatalized',
 'nasalized_preglottalized',
 'palatalized',
 'palatalized_prenasalized',
 'pharyngealized',
 'pharyngealized_glottalized',
 'pharyngealized_labialized',
 'plain',
 'postnasalized',
 'preglottalized',
 'prenasalized',
 'prenasalized_rhotic',
 'pulmonic_ingressive',
 'q_accompaniment',
 'r_accompaniment',
 'rhotic',
 's_accompaniment',
 'strident',
 'syllabic',
 't_accompaniment',
 'tense',
 'trilled',
 'velar_prenasalized',
 'velarized',
 'voiced_aspirated',
 'voiceless',
 'voiceless_nasalized',
 'voiceless_prenasalized',
 'x_accompaniment',
 'z_accompaniment']

