import simpleder

# reference (ground truth)
ref = [("A", 0.0, 1.0),
       ("B", 1.0, 1.5),
       ("A", 1.6, 2.1)]

# hypothesis (diarization result from your algorithm)
hyp = [("1", 0.0, 0.8),
       ("2", 0.8, 1.4),
       ("3", 1.5, 1.8),
       ("1", 1.8, 2.0)]

error = simpleder.DER(ref, hyp)

print("DER={:.3f}".format(error))