from dotenv import load_dotenv

_ = load_dotenv()


def main():
    from langchain_core.prompts import PromptTemplate
    from langchain_ollama import ChatOllama

    print("Hello from langchain-course!")
    information = """
    
Elon Musk
FRS

Musk in 2025
CEO of SpaceX
Incumbent
Assumed office
March 14, 2002
Preceded by	Position established
CEO of Tesla Inc.
Incumbent
Assumed office
October 2008
Preceded by	Ze'ev Drori
Senior Advisor to the President for Government Efficiency
In office
January 20, 2025 – May 30, 2025
Serving with Massad Boulos
President	Donald Trump
Personal details
Born	Elon Reeve Musk
June 28, 1971 (age 55)
Pretoria, South Africa
Citizenship	
South Africa (since 1971)
Canada (since 1971)
United States (since 2002)
Party	Independent[a]
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Children	14,[b] including Vivian Wilson
Parents	
Errol Musk (father)
Maye Musk (mother)
Relatives	Musk family
Education	University of Pennsylvania (BA, BS)
Occupation	
CEO and product architect of Tesla
Founder, CEO, and chief engineer of SpaceX
Founder and CEO of xAI
Founder and CTO of X Corp.
Co-founder of Neuralink, The Boring Company, OpenAI, Zip2, X.com and PayPal
President of the Musk Foundation
Awards	Full list
Signature	
Musk's voice
Duration: 3 minutes and 10 seconds.3:10
Musk on his main goals for SpaceX and the future of human civilization
Recorded January 22, 2026
	
This article is part of
a series about
Elon Musk
Personal
Companies
Politics
In the arts and media
vte
Elon Reeve Musk (/ˈiːlɒn/ ⓘ EE-lon; born June 28, 1971) is a businessman and former public official who is the CEO and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only trillionaire in terms of US dollars in June 2026; as of July 23, 2026, Forbes estimates his net worth to be US$744 billion.

Born into the wealthy Musk family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. In 1995, Musk co-founded Zip2, a web software company. Following its sale in 1999, he co-founded X.com, an e-commerce payment system that merged with Confinity in March 2000 to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002.
    """
    summary_template = """
    Given the information {information} about a person, create a short summary.
    Format the response as bullet points only:
    - One short summary point
    - Two interesting facts about the person (each as its own bullet point)
    """
    summary_prompt_template = PromptTemplate(template=summary_template, input_variables=["information"])
    llm = ChatOllama(model="gemma3:270m", temperature=0)
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
