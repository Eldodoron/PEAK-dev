with open(r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\panoptic\inspections.json", "rb") as f:
    chunk = f.read(500)
print("Header:", repr(chunk[:100]))
