        <section class="container">
            % info = result['info']
            % article = result['article']
            % categories = result['category']
            <div class="col-sm-12">
                <h3>記事作成</h3>
                <div class="box">
                    <form id="form" action="/blog/admin/create_article" method="post">
                        <input type="hidden" name="id" id="id" value="{{article.id}}">
                        <input type="hidden" name="info_id" id="info_id" value="{{info.id}}">
                        <table class="table">
                            <tr class="row">
                                <th width="100px">記事名<span class="required">*</span></th>
                                <td>
                                    <input type="text" name="title" id="title" value="{{article.title}}">
                                    % if 'error' in result and result['error'].have('title'):
                                        <label class="error">{{result['error'].get('title')['message']}}</label>
                                    % end
                                </td>
                            </tr>
                            <tr class="row">
                                <th width="100px">記事<span class="required">*</span></th>
                                <td>
                                    <textarea name="article" id="article" class="mceAdvanced" rows="20">{{article.article}}</textarea>
                                </td>
                            </tr>
                            <tr class="row">
                                <th width="100px">カテゴリ</th>
                                <td>
                                    <select id="category" name="category">
                                        <option value="0">カテゴリなし</option>
                                    % for category in categories:
                                        % if category.id == article.category_id:
                                            <option value="{{category.id}}" selected>{{category.name}}</option>
                                        % else:
                                            <option value="{{category.id}}">{{category.name}}</option>
                                        % end
                                    % end
                                    </select>
                                </td>
                            </tr>
                        </table>
                        <input type="submit">
                    </form>
                </div>
            </div>
        </section>
