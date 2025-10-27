## Test sentences

Self-selected from the test set (Elicitation mostly? VV-ARS)

La casa está ardiendo    The house is on fire    CASA COCINAR
Los niños nos dan los libros    The boys give us the books    HOMBRE PEQUEÑO2 REVISTA cl.m(B):recibir-montón INDX.PRO:1pl
PADRE^MADRE INDX BEBÉ INDX DAR NOMBRE ANA
HOMBRE PERSONA HABITACIÓN LLENAR cl.d(B):llenar-caja cl.m(B):llevar-caja DÓNDE MERCADO cl.e(B):LOCALIZACIÓN

## Models

Gemini-2.5-Pro, free trial but £18.99/month or 5 requests-ish (0-shot length) per day

## Prompts

Advised by Langchain (for the *** structure), Tanzer et al. (2024), Merx et al. (2024), and Aycock et al. (2025).

### 0-shot EN-LSE Text2Gloss (mostly built on Aycock et al., (2025))

You are a text-to-text translator for Spanish Sign Language (or Lengua de Signos Española, LSE) which only produces or accepts LSE data in Sign Language gloss format. LSE is a sign language primarly used in Spain and is considered a language isolate (ISO 639-3 code ssp, glottocode span1263).

Translate the following sentence from English to LSE glosses: "{EN_source}"

Do not say that you do not know LSE. Do not say you do not have enough information, you must make a guess. If your translation is wrong, that is fine, but you have to provide a translation.

Your translation must be the first line of your response only, with no text before the translation. If it is necessary, only provide your reasoning on subsequent lines after providing the translation.

It is crucial that you only give the translation on the first line of your response, otherwise you will fail. Now write the translation:

English: "{EN_source}" LSE: 

### 0-shot LSE-EN Gloss2Text

You are a text-to-text translator for Spanish Sign Language (or Lengua de Signos Española, LSE) which only produces or accepts LSE data in Sign Language gloss format. LSE is a sign language primarly used in Spain and is considered a language isolate (ISO 639-3 code ssp, glottocode span1263).

Translate the following sentence from LSE glosses to English: "{LSE_source}"

Do not say that you do not know LSE. Do not say you do not have enough information, you must make a guess. If your translation is wrong, that is fine, but you have to provide a translation.

Your translation must be the first line of your response only, with no text before the translation. If it is necessary, only provide your reasoning on subsequent lines after providing the translation.

It is crucial that you only give the translation on the first line of your response, otherwise you will fail. Now write the translation:

LSE: "{LSE_source}" English: 


### Parallel sentences in the prompt (S-p) EN-LSE Text2Gloss (mostly built on Aycock et al. (2025) full wordlist/parallel sentences unlike MTOB k nearest)

(the same as 0-shot, but will additions appended) (order permuted) (MTOB finds nearest 2 sentences)

—
To help with the translation, here is a list of parallel sentences in English and LSE glosses:

*** Parallel English-LSE sentences text ***
—

(long processing time, around 1 minute)


### Parallel sentences in an attachment (S-a) EN-LSE Text2Gloss (mostly built on Aycock et al. (2025))


### Wordlist in the prompt (W-p) (mostly built on Aycock et al. (2025) full wordlist/parallel sentences unlike MTOB k nearest)

—
To help with the translation, here is a word list with LSE glosses and equivalent Spanish words:

*** Spanish-LSE Wordlist text ***
—


### Grammar text prompts (G-p)

(cannot share though, so more open source would be required) (A "scan of a PDF version" converted to text with pdftotext lib with -layout flag then post-editing corrupted bits, front and back matter, references, and then paragraph-ising text)

(extremely long processing time, in the order of 5-10 minutes) (also shows the difference in glosses bc of non standardisation) (GAVE UP on PROMPT)


### All prompts (G-a)

(same as above but grammar book as 880k attachment)
(response gives sources to text)



(Grammar book as PDF or text?) (kept text because pdf is 100MiB and text is 800KiB)


### Human condition

