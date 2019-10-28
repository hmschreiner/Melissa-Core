from collections import namedtuple
import t800.actions_db as actions_db

text_list = 'qual a previsao do tempo para hoje?'.split()
zlist = zip(text_list, list(range(len(text_list))))

print(zlist)

# # Clear the expression table for each new user expression.
# actions_db.cur.execute('DELETE FROM expression')

# # Insert expression words in to SQLite. A word may appear more
# # than once in the expression. Only the first occurence will
# # be kept.
# actions_db.cur.executemany("INSERT OR IGNORE INTO expression "
#                            "values (?,?)", zlist)
# actions_db.con.commit()

# # Match multiple-word groups against the expression words.
# sql = "SELECT e.word, e.word_order, "\
#     + "  g.word_group, g.word_count, g.function "\
#     + "FROM expression e "\
#     + "JOIN words w "\
#     + "ON w.word = e.word "\
#     + "JOIN word_groups g "\
#     + "ON g.word_group = w.word_group "\
#     + "WHERE g.word_count > 1 "\
#     + "ORDER BY e.word_order, g.word_group"

# actions_db.cur.execute(sql)
# rows = actions_db.cur.fetchall()

# # Make the following easier to read using namedtuple.
# sql_row_def = namedtuple('sql_row_def', 'word, word_order, word_group, word_count, function') # noqa
# scoring = {}
# for row in rows:
#     sql_row = sql_row_def._make(row)
#     print(row)
