#!/usr/bin/env python3
"""LC templates and snippets"""

solution = '''#!/usr/bin/env python3
"""{prob_url}"""

from tools.lc_tools import benchmark, init_solutions, pretty_eval


class SolutionInit:
    # Time / Space:
    def {func_sig}:
        pass


class SolutionPref:
    # Time / Space:
    def {func_sig}:
        pass


if __name__ == '__main__':
    # Setup
    solutions = init_solutions(globals())
    method = '{func_name}'
    
    # Examples
    inputs = {inputs}
    outputs = {outputs}
    pretty_eval(solutions, method, inputs, outputs)

    # Benchmarking
    number = 250
    args = {benchmark_input}
    benchmark(solutions, method, args, number)
'''


review = '''#!/usr/bin/env python3
"""{prob_url}"""

class Solution:
    def {func_sig}:
        pass
'''


sig = '''{method}(self, {params}) -> {ret_type}'''


io = '''    # Example {n} (Expected Output: {o})
    {i}
    print(s_init.{func_name}({input_syms}))
    print(s_pref.{func_name}({input_syms}))'''


readme = '''### [{title}]({prob_url}) ([solutions]({solutions_url})) 🙃😎🤯

|       Date       | Think | Code | Total |         Language         |
|:----------------:|:-----:|:----:|:-----:|:------------------------:|
'''


anki = '''LeetCode<br><br><a href="{prob_url}">{title}</a>'''

graphql_query = '''query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    boundTopicId
    title
    titleSlug
    content
    translatedTitle
    translatedContent
    isPaidOnly
    canSeeQuestion
    difficulty
    likes
    dislikes
    isLiked
    similarQuestions
    exampleTestcases
    categoryTitle
    contributors {
      username
      profileUrl
      avatarUrl
      __typename
    }
    topicTags {
      name
      slug
      translatedName
      __typename
    }
    companyTagStats
    codeSnippets {
      lang
      langSlug
      code
      __typename
    }
    stats
    hints
    solution {
      id
      canSeeDetail
      paidOnly
      hasVideoSolution
      paidOnlyVideo
      __typename
    }
    status
    sampleTestCase
    metaData
    judgerAvailable
    judgeType
    mysqlSchemas
    enableRunCode
    enableTestMode
    enableDebugger
    envInfo
    libraryUrl
    adminUrl
    challengeQuestion {
      id
      date
      incompleteChallengeCount
      streakCount
      type
      __typename
    }
    __typename
  }
}
'''
