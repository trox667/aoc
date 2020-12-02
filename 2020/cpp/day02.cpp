#include <cassert>
#include <fstream>
#include <iostream>
#include <regex>
#include <vector>

struct Entry {
  std::string password;
  char letter;
  int min;
  int max;
};

static const std::string pattern = "(\\d+)-(\\d+) ([A-z]): ([A-z]+)";
void parse(const std::string &line, Entry &entry) {
  std::regex regex(pattern);
  std::smatch matches;
  std::regex_search(line, matches, regex);
  if (matches.size() == 5) {
    auto password = matches[4].str();
    auto c = matches[3].str();
    auto min = std::stoi(matches[1].str());
    auto max = std::stoi(matches[2].str());
    entry.password = password;
    entry.letter = c.front();
    entry.min = min;
    entry.max = max;
  }
}

int char_count(const std::string &password, const char letter) {
  int count = 0;
  for (auto s : password)
    if (s == letter)
      count++;
  return count;
}

bool policy_min_max(const std::string &password, const char letter,
                    const int min, const int max) {
  int count = char_count(password, letter);
  return min <= count && count <= max;
}

bool match_policy_min_max(const Entry &entry) {
  return policy_min_max(entry.password, entry.letter, entry.min, entry.max);
}

int run(const std::vector<Entry> &entries) {
  int count = 0;
  for (auto entry : entries)
    if (match_policy_min_max(entry))
      count++;
  return count;
}

void read_input(std::vector<Entry> &entries) {
  std::ifstream in("../inputs/input02");
  std::string str;
  while (std::getline(in, str)) {
    if (str.find_first_not_of(' ') != std::string::npos) {
      Entry entry;
      parse(str, entry);
      entries.push_back(entry);
    }
  }
}

void part1() {
  std::vector<Entry> entries;
  read_input(entries);
  std::cout << run(entries) << std::endl;
}

bool char_pos(const std::string &password, const char letter, const int pos) {
  assert(0 <= pos && pos <= password.size());
  return password.at(pos - 1) == letter;
}

bool policy_position(const std::string &password, const char letter,
                     const int min, const int max) {
  return char_pos(password, letter, min) ^ char_pos(password, letter, max);
}

bool match_policy_position(const Entry &entry) {
  return policy_position(entry.password, entry.letter, entry.min, entry.max);
}

int run2(const std::vector<Entry> &entries) {
  int count = 0;
  for (auto entry : entries)
    if (match_policy_position(entry))
      count++;
  return count;
}

void part2() {
  std::vector<Entry> entries;
  read_input(entries);
  std::cout << run2(entries) << std::endl;
}

void test_parse() {
  Entry entry;
  parse("1-3 a: abcde", entry);
  assert(entry.letter == 'a');
  assert(entry.password == "abcde");
  assert(entry.min == 1);
  assert(entry.max == 3);
}

void test_char_count() {
  assert(char_count("abcde", 'a') == 1);
  assert(char_count("ccccccccc", 'c') == 9);
}

int main(void) {
  test_parse();
  test_char_count();
  part1();
  part2();
  return 0;
}
