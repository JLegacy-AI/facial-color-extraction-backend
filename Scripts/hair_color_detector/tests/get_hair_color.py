from hair_color_detector import HairColorDetector



if __name__ == "__main__":
    hcd = HairColorDetector()
    result = hcd.get_color('blue_medium.jpg',  save_result=False, n_clusters=3)
    print(result)


