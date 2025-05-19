from deep_translator import GoogleTranslator

def main():
    print("Hexrail Translate")
    print("Type 'exit' anytime to quit.\n")

    while True:
        source = input("From language (e.g., 'en', 'tr', 'de'): ").lower()
        if source == 'exit':
            print("👋 Goodbye.")
            break

        target = input("To language (e.g., 'en', 'fr', 'ar'): ").lower()
        if target == 'exit':
            print("👋 Goodbye.")
            break

        text = input("Text to translate: ")
        if text.lower() == 'exit':
            print("👋 Goodbye.")
            break

        try:
            translated = GoogleTranslator(source=source, target=target).translate(text)
            print(f"📝 Translated ({source} → {target}): {translated}\n")
        except Exception as e:
            print("❌ Error:", str(e), "\n")

if __name__ == "__main__":
    main()
