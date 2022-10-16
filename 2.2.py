def main():
    s = ' '.join(input().strip().lower().split()[::-1]).capitalize()
    print(s)
if __name__ == "__main__":
    main()